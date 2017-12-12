#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
print string.ascii_letters
[u'\n', u''][skip_eol])
print (u'%s%s' % (message, [u'\n', u''][skip_eol])).encode(locale.getpreferredencoding()),
request = urllib2.Request(self._LANG_URL, None, std_headers)
		try:
			self.report_lang()
			urllib2.urlopen(request).read()
			
return _opener.open(url, data, timeout)

 def open(self, fullurl, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        # accept a URL or a Request object
        if isinstance(fullurl, basestring):
            req = Request(fullurl, data)
        else:
            req = fullurl
            if data is not None:
                req.add_data(data)

        req.timeout = timeout
        protocol = req.get_type()#http

        # pre-process request
        meth_name = protocol+"_request" #http_request
        for processor in self.process_request.get(protocol, []): #process_request是个词典，processor是个HTTPHandler
            meth = getattr(processor, meth_name)
            req = meth(req)

        response = self._open(req, data)

        # post-process response
        meth_name = protocol+"_response"
        for processor in self.process_response.get(protocol, []):
            meth = getattr(processor, meth_name)
            response = meth(req, response)

        return response
        
            def proxy_open(self, req, proxy, type):
        orig_type = req.get_type()
        proxy_type, user, password, hostport = _parse_proxy(proxy)

        if proxy_type is None:
            proxy_type = orig_type

        if req.host and proxy_bypass(req.host):
            return None

        if user and password:
            user_pass = '%s:%s' % (unquote(user), unquote(password))
            creds = base64.b64encode(user_pass).strip()
            req.add_header('Proxy-authorization', 'Basic ' + creds)
        hostport = unquote(hostport)
        req.set_proxy(hostport, proxy_type)

        if orig_type == proxy_type or orig_type == 'https':
            # let other handlers take care of it
            return None
        else:
            # need to start over, because the other handlers don't
            # grok the proxy's URL type
            # e.g. if we have a constructor arg proxies like so:
            # {'http': 'ftp://proxy.example.com'}, we may end up turning
            # a request for http://acme.example.com/a into one for
            # ftp://proxy.example.com/a
            return self.parent.open(req, timeout=req.timeout)
            
                def http_response(self, request, response):
        self.cookiejar.extract_cookies(response, request)
        return response
        
        
            def http_response(self, request, response):
        self.cookiejar.extract_cookies(response, request)
        return response 
        
            return _opener.open(url, data, timeout) ##返回response类型
            
                    s = self.fp.read(amt) ##httplib.py里面
                    
def read(self, amt=None):## ##httplib.py里面
        if self.fp is None:
            return ''

        if self.chunked:
            return self._read_chunked(amt)

        if amt is None:
            # unbounded read
            if self.length is None:
                s = self.fp.read()
            else:
                s = self._safe_read(self.length)
                self.length = 0
            self.close()        # we read everything
            return s #返回后调用 data = self._sock.recv(rbufsize)

        if self.length is not None:
            if amt > self.length:
                # clip the read to the "end of response"
                amt = self.length

        # we do not use _safe_read() here because this may be a .will_close
        # connection, and the user is reading more bytes than will be provided
        # (for example, reading in 1k chunks)
        s = self.fp.read(amt)
        if self.length is not None:
            self.length -= len(s)
            if not self.length:
                self.close()
        return s
        
def read(self, size=-1):##socket.py里面
        # Use max, disallow tiny reads in a loop as they are very inefficient.
        # We never leave read() with any leftover data from a new recv() call
        # in our internal buffer.
        rbufsize = max(self._rbufsize, self.default_bufsize)
        # Our use of StringIO rather than lists of string objects returned by
        # recv() minimizes memory usage and fragmentation that occurs when
        # rbufsize is large compared to the typical return value of recv().
        buf = self._rbuf
        buf.seek(0, 2)  # seek end
        if size < 0:
            # Read until EOF
            self._rbuf = StringIO()  # reset _rbuf.  we consume it via buf.
            while True:
                data = self._sock.recv(rbufsize)
                if not data:
                    break
                buf.write(data)
            return buf.getvalue()
        else:
            # Read until size bytes or EOF seen, whichever comes first
            buf_len = buf.tell()
            if buf_len >= size:
                # Already have size bytes in our buffer?  Extract and return.
                buf.seek(0)
                rv = buf.read(size)
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return rv

            self._rbuf = StringIO()  # reset _rbuf.  we consume it via buf.
            while True:
                left = size - buf_len
                # recv() will malloc the amount of memory given as its
                # parameter even though it often returns much less data
                # than that.  The returned data string is short lived
                # as we copy it into a StringIO and free it.  This avoids
                # fragmentation issues on many platforms.
                data = self._sock.recv(left)
                if not data:
                    break
                n = len(data)
                if n == size and not buf_len:
                    # Shortcut.  Avoid buffer data copies when:
                    # - We have no data in our buffer.
                    # AND
                    # - Our call to recv returned exactly the
                    #   number of bytes we were asked to read.
                    return data
                if n == left:
                    buf.write(data)
                    del data  # explicit free
                    break
                assert n <= left, "recv(%d) returned %d bytes" % (left, n)
                buf.write(data)
                buf_len += n
                del data  # explicit free
                #assert buf_len == buf.tell()
            return buf.getvalue()
            
                while True:##socket.py里面
                data = self._sock.recv(rbufsize)
                
                response = self._open(req, data)# 返回addinfourl对象，即增加fp对象
                
def _open(self, req, data=None):
        result = self._call_chain(self.handle_open, 'default',
                                  'default_open', req)
        if result:
            return result

        protocol = req.get_type()
        result = self._call_chain(self.handle_open, protocol, protocol +
                                  '_open', req)
        if result:
            return result

        return self._call_chain(self.handle_open, 'unknown',
                                'unknown_open', req)
                                
                                
        token = urllib.unquote(mobj.group(1))#替换unicode符号
        
        video_uploader = urllib.unquote(mobj.group(1)) #CSPAN
        
        
        ie.extract(url)