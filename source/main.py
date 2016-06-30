#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        f = open('home.html')
        f = f.read()
        self.response.write(f)
class NewsHandler(webapp2.RequestHandler):
    def get(self):
        f = open('devlog.html')
        f = f.read()
        self.response.write(f)
class ForumHandler(webapp2.RequestHandler):
    def get(self):
        f = open('forum.html')
        f = f.read()
        self.response.write(f)
class WikiHandler(webapp2.RequestHandler):
    def get(self):
        f = open('wiki.html')
        f = f.read()
        self.response.write(f)
class ForumDevsHandler(webapp2.RequestHandler):
    def get(self):
        f = open('forumdevs.html')
        f = f.read()
        self.response.write(f)
app = webapp2.WSGIApplication([
    ('/', HomeHandler),('/news', NewsHandler),('/forum',ForumHandler),('/wiki',WikiHandler),('/forum/devs', ForumDevsHandler)
], debug=True)
