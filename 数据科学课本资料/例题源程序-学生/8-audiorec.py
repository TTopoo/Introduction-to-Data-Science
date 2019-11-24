#例8-3： 使用百度API识别语音对应文本

from aip import AipSpeech      #导入语音识别包
def get_file_content(file_name):          #从文件中提取语音内容
    with open(file_name, 'rb') as fp:
        return fp.read()

APP_ID = '10694657'
API_KEY = 'qtCumlQUdEk4dKpZItWFGY6a'
SECRET_KEY = 'bab91297af93124058a910c2c962ccae'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)#初始化识别模型
file_name='data/voice.wav'           #语音文件
result = aipSpeech.asr(get_file_content(file_name), 'wav', 16000, {'dev_ip': '1536'})
print (result['result'][0])
