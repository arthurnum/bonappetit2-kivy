from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import urllib.parse
import time
import json

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text = 'Do')
        button.bind(on_press = self.do_button_on_press)
        layout.add_widget(button)
        layout.add_widget(Label(text = 'Response:'))
        self.response_label = Label(text = '<empty>')
        layout.add_widget(self.response_label)
        return layout

    def do_button_on_press(obj, sender):
        params = urllib.parse.urlencode({'timestamp': 23452345345, 'page': 1, 'per_page': 25})
        headers = {'X-Api-Uuid': '-n-W4Z9N42zGXy4a', 'X-Api-Access-Token': 'c2f1c510a7ca24c7f5bad1b9262b55bc'}
        # req = UrlRequest(url='http://ba.dev.orangesoft.by:80/api/v1/updates.json?', on_failure=obj.process_response, req_body=params, req_headers=headers, method='GET')
        req = UrlRequest(url='https://test.bonappetit2.s3.amazonaws.com/uploads/staging/update/file/2015/04/28/15/1430223801.zip', file_path='/home/arthurnum/kividone', on_success=obj.process_response, method='GET')
        obj.response_label.text = "process..."

    def process_response(obj, req, results):
        result = ''
        # for key, value in results.items():
        #     result += key + ': \n'
        #     for a in value:
        #         for k, v in a.items():
        #             result += k + v + '\n'
        obj.response_label.text = result


TestApp().run()
