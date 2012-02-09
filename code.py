#!/usr/bin/env python

import sys
sys.path.append('/home/staff/meyersh/git/webpy')

import web

class index:
  def GET(self):
    return "Hello, world!"


urls = (
  '/', 'index'
  )

app = web.application(urls, globals())

if __name__ == "__main__":
  app.run()
