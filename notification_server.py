import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import telebot


BOT_TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='markdown')


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        self._set_headers()
        try:
            cid = int(self.path[1:])
        except Exception as e:
            self.wfile.write('Invalid cid {}'.format(self.path).encode('utf-8')) 
            return
        if len(post_data) > 10000:
            self.wfile.write('Invalid data')
            return
        print('Chat {} data {}'.format(cid, post_data))
        bot.send_message(cid, '`' + post_data + '`')

def run(server_class=HTTPServer, handler_class=S, port=18880):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
