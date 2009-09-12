class AMEEConnection:

  def __init__(self, server, username = None, password = None, use_json_if_available = True, enable_caching = False, enable_debug = False):
    self.server = server
    self.username = username
    self.password = password
    self.auth_token = None
    self.use_json_if_available = use_json_if_available
    if (self.username or self.password) and not self.valid():
     raise "Must specify both username and password for authenticated access"
    self.enable_caching = enable_caching
    #if self.enable_caching
      #$cache ||= {}
    #end
    # Make connection to server
    #self.http = Net::HTTP.new(@server)
    #self.http.read_timeout = 5
    #self.http.set_debug_output() if enable_debug

#  def timeout(self):
#    @http.read_timeout
#
#  def timeout=(self, t):
#    @http.read_timeout = t

  def valid(self):
    if (self.username or self.password):
      return self.username != None and self.password != None and self.server != None
    else:
      return self.server != None

  def can_authenticate(self):
    return self.username != None and self.password != None

  def authenticated(self):
    return self.auth_token != None

#  def get(self, path, data = {}):
#    # Create URL parameters
#    params = []
#    data.each_pair do |key, value|
#      params << "#{key}=#{value}"
#    end
#    if params.size > 0
#      path += "?#{params.join('&')}"
#    end
#    # Send request
#    #return $cache[path] if @enable_caching and $cache[path]
#    response = do_request Net::HTTP::Get.new(path)
#    #$cache[path] = response if @enable_caching
#    return response
#
#  def post(self, path, data = {}):
#    clear_cache
#    # Create POST request
#    post = Net::HTTP::Post.new(path)
#    body = []
#      data.each_pair do |key, value|
#      body << "#{key}=#{value}"
#    end
#    post.body = body.join '&'
#    # Send request
#    do_request(post)
#
#  def put(path, data = {}):
#    clear_cache
#    # Create PUT request
#    put = Net::HTTP::Put.new(path)
#    body = []
#      data.each_pair do |key, value|
#      body << "#{key}=#{value}"
#    end
#    put.body = body.join '&'
#    # Send request
#    do_request(put)
#
#  def delete(path):
#    clear_cache
#    # Create DELETE request
#    delete = Net::HTTP::Delete.new(path)
#    # Send request
#    do_request(delete)
#
#  def authenticate:
#    unless can_authenticate?
#      raise AMEE::AuthRequired.new("Authentication required. Please provide your username and password.")
#    end
#    response = nil
#    post = Net::HTTP::Post.new("/auth")
#    post.body = "username=#{@username}&password=#{@password}"
#    post['Accept'] = content_type
#    response = @http.request(post)
#    @auth_token = response['authToken']
#    unless authenticated?
#      raise AMEE::AuthFailed.new("Authentication failed. Please check your username and password.")
#    end
#
#    protected
#
#  def content_type:
#    (@use_json_if_available && defined?(JSON)) ? 'application/json' : 'application/xml'
#
#  def redirect?(response):
#    response.code == '301' || response.code == '302'
#
#  def response_ok?(response):
#    case response.code
#      when '200'
#        return true
#      when '403'
#        raise AMEE::PermissionDenied.new("You do not have permission to perform the requested operation")
#      when '401'
#        authenticate
#        return false
#      else
#        raise AMEE::UnknownErr(self)or.new("An error occurred while talking to AMEE: HTTP response code #{response.code}")
#
#  def do_request(request):
#    # Open HTTP connection
#    @http.start
#    # Do request
#    begin
#      response = send_request(request)
#    end while !response_ok?(response)
#    # Return body of response
#    return response.body
#  rescue SocketError
#    raise AMEE::ConnectionFailed.new("Connection failed. Check server name or network connection.")
#  ensure
#    # Close HTTP connection
#    @http.finish if @http.started?
#
#  def send_request(self, request):
#    request['authToken'] = @auth_token
#    request['Accept'] = content_type
#    response = @http.request(request)
#    # Handle 404s
#    if response.code == '404'
#      raise AMEE::NotFound.new("URL doesn't exist on server.")
#    end
#    # Done
#    response
#
#  def clear_cache(self):
#    if @enable_caching
#      $cache = {}
#    end