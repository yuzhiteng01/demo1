#!/usr/bin/python
#coding=utf8

from django.core import serializers
from django import http
import multiprocessing


from django.views.generic import TemplateView, ListView
from django.core.serializers.json import DjangoJSONEncoder

import os
import json
import base64
import socket
import paramiko
import traceback
import platform


def trace_back():
    try:
        return traceback.format_exc()
    except:
        return ''
    

#设置日志记录
sys = platform.system()
if sys == 'Windows':
    paramiko.util.log_to_file('H:\dev_devops\\test.log')
elif sys == 'Linux':
    paramiko.util.log_to_file('/tmp/test')


def ssh_cmd(host):

   
    #建立连接
    ssh=paramiko.SSHClient()
        
    try:
    
        #如果没有密码就走public key
        if host.get('passwd',True) == True:
            
            privatekeyfile = os.path.expanduser('/root/.ssh/id_rsa')
            paramiko.RSAKey.from_private_key_file(privatekeyfile)

        if host.get('port',True) == True:
            host['port'] = 22


        #缺失host_knows时的处理方法
        known_host = "/root/.ssh/known_hosts"
        ssh.load_system_host_keys(known_host)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


        #连接远程客户机器
        try:
            ssh.connect(
                        hostname =host['inner_ip'],
                        port     =int(host['port']),
                        username =host['username'],
                        password =host['passwd'],
                        compress =True,
                        timeout  =300
                        )
        except:
            ssh.connect(
                    hostname =host['public_ip'],
                    port     =int(host['port']),
                    username =host['username'],
                    password =host['passwd'],
                    compress =True,
                    timeout  =300
                    )
            
     
        #获取远程命令执行结果
        stdin, stdout, stderr = ssh.exec_command(host['cmd'],bufsize=65535, timeout=300)
        temp = stdout.readlines()
        
        status = {'status':0,'output':json.dumps(temp)}
        
        #输出执行结果
        ssh.close()

        return status
 
    except  :

        ssh.close()

        return {'status':-1,'output':trace_back()}
        

def ssh_cmd2(data):

    import commands

    cmd = "uptime"

    if data.get('passwd',True) == True:

        cmd = '''ssh -o StrictHostKeyChecking=no -p 22 %(username)s@%(public_ip)s "%(cmd)s"'''%data
    else:

        cmd = '''sshpass -p '%(passwd)s' ssh -o StrictHostKeyChecking=no -p 22 %(username)s@%(public_ip)s "%(cmd)s"'''%data

    (status,output) = commands.getstatusoutput(cmd)

    return {'status':status,'output':output}


class JSONResponseMixin(object):
    """JSON mixin"""


    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        return http.HttpResponse(content,
                            content_type='application/json',
                            **httpresponse_kwargs)

    def convert_context_to_json(self, context):

        #return serializers.serialize("json", context)
        
        return json.dumps(context,cls=DjangoJSONEncoder)




class SSHJsonView(JSONResponseMixin, TemplateView):

    hosts = []
    message = []

    def get(self, request, *args, **kwargs):

        pool = multiprocessing.Pool(processes = 10)
        result = []


        for host in SSHJsonView.hosts:
         
            result.append(pool.apply_async(ssh_cmd, (host,)))

        pool.close()
        pool.join()

        msg = []
        for res in result:
            msg.append(res.get())


        SSHJsonView.message = json.dumps(msg,cls=DjangoJSONEncoder)

       



class MainCategoryJsonView(JSONResponseMixin, TemplateView):



    def get(self, request, *args, **kwargs):

        from models.service.main_category import ServiceMainCategory

        data = ServiceMainCategory.get_maincategory(request)

        return self.render_to_response(data)




class ClusterJsonView(JSONResponseMixin, TemplateView):


    def get(self, request, *args, **kwargs):

        from models.service.clusters import ServiceClusters

        data = ServiceClusters.get_clusters(request)

        return self.render_to_response(data)

class PlatFormJsonView(JSONResponseMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        '''
        获取平台并判断可部署的项目权限
        '''

        print '000000000000000555555555'
        from models.service.platform import ServicePlatform
        print '33333333333333333'
        data = ServicePlatform.get_platform(request)
        result = []
        print 'data:', data
        print 'request.session["user_role"]', request.session["user_role"]
        print 'request.session["userproject"]', request.session["userproject"]

        if request.session["user_role"]== "user":
            for k in data:
                for v in request.session["userproject"]:

                    if k['prefix'] == v['alias'].strip():
                        k['git_addr'] = v['git_addr'].strip() if v['git_addr'] else ''
                        result.append(k)
        else:
            for v in request.session["userproject"]:
                for ind, k in enumerate(data):
                    if k['prefix'] == v['alias'].strip():
                        data[ind]['git_addr'] = v['git_addr']
                        result.append(data[ind])

        print 'result11111:', result
        return self.render_to_response(result)
class ChannelJsonView(JSONResponseMixin, TemplateView):


    def get(self, request, *args, **kwargs):

        from models.service.channel import ServiceChannel

        data = ServiceChannel.get_channel()

        return self.render_to_response(data)


class AppIdJsonView(JSONResponseMixin, TemplateView):


    def get(self, request, *args, **kwargs):

        from models.service.appid import ServiceAppId

        data = ServiceAppId.get_appid(request)

        return self.render_to_response(data)



class ServicesJsonView(JSONResponseMixin, TemplateView):

    def get(self, request, *args, **kwargs):

        from models.service.game_server import ServiceGameServer

        data = ServiceGameServer.get_services(request)

        return self.render_to_response(data)


class GameModuleJsonView(JSONResponseMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        from models.service.game_module import ServiceGameModule
        data = ServiceGameModule.get_game_module(request)
        return self.render_to_response(data)
class AssetsJsonView(JSONResponseMixin, TemplateView):

    def post(self, request, *args, **kwargs):
        from models.service.assets import ServiceAssets

        data = ServiceAssets.get_assets(request)

        return self.render_to_response(list(data))
