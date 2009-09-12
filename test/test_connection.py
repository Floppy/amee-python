from amee import *
from nose.tools import *

class TestAmeeConnection:
  
  def test_can_be_created_with_url_only(self):
    #flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
    c = AMEEConnection('server.example.com')
    assert c.valid() == True
  
  @raises()
  def test_cannot_be_created_with_username_but_no_password(self):
    #flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
    AMEEConnection('server.example.com', 'username')

#  it "cannot be created with password but no username" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
#    lambda{AMEE::Connection.new('server.example.com', nil, 'password')}.should raise_error
#  end
#
  def test_can_be_created_with_url_username_and_password(self):
    #flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
    c = AMEEConnection('server.example.com', 'username', 'password')
    assert c.valid() == True
#
#  it "has default timeout of 5 seconds" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
#    c = AMEE::Connection.new('server.example.com')
#    c.timeout.should be(5)
#  end
#
#  it "can set timeout" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
#    c = AMEE::Connection.new('server.example.com')
#    c.timeout = 30
#    c.timeout.should be(30)
#  end
#
#end

  def test_should_start_out_unauthenticated(self):
    #flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
    c = AMEEConnection('server.example.com', 'username', 'password')
    assert c.authenticated() == False

  def test_should_be_capable_of_authentication(self):
    #flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
    c = AMEEConnection('server.example.com', 'username', 'password')
    assert c.can_authenticate() == True

#  def test_should_be_able_to_get_private_urls(self):
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '401', :body => ''),
#                                               flexmock(:code => '200', :body => '', :'[]' => 'dummy_auth_token_data'),
#                                               flexmock(:code => '200', :body => '<?xml version="1.0" encoding="UTF-8"?><Resources><DataCategoryResource><Path/><DataCategory created="2007-07-27 09:30:44.0" modified="2007-07-27 09:30:44.0" uid="CD310BEBAC52"><Name>Root</Name><Path/><Environment uid="5F5887BCF726"/></DataCategory><Children><DataCategories><DataCategory uid="BBA3AC3E795E"><Name>Home</Name><Path>home</Path></DataCategory><DataCategory uid="9E5362EAB0E7"><Name>Metadata</Name><Path>metadata</Path></DataCategory><DataCategory uid="6153F468BE05"><Name>Test</Name><Path>test</Path></DataCategory><DataCategory uid="263FC0186834"><Name>Transport</Name><Path>transport</Path></DataCategory><DataCategory uid="2957AE9B6E6B"><Name>User</Name><Path>user</Path></DataCategory></DataCategories></Children></DataCategoryResource></Resources>'))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEEConnection('server.example.com', 'username', 'password')
#    response = amee.get('/data')
#    assert response != ""
#    assert amee.authenticated == True

#  it "should handle 404s gracefully" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil, :request => flexmock(:code => '404', :body => ""), :finish => nil)
#    amee = AMEE::Connection.new('server.example.com', 'username', 'password')
#    lambda{amee.get('/missing_url')}.should raise_error(AMEE::NotFound, "URL doesn't exist on server.")
#  end
#
#  it "should raise error if permission for operation is denied" do
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '403', :body => ''))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEE::Connection.new('server.example.com', 'username', 'password')
#    lambda {
#      amee.get('/data')
#    }.should raise_error(AMEE::PermissionDenied,"You do not have permission to perform the requested operation")
#  end
#
#  it "should raise error if authentication succeeds, but permission for operation is denied" do
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '401', :body => ''),
#                                               flexmock(:code => '200', :body => '', :'[]' => 'dummy_auth_token_data'),
#                                               flexmock(:code => '403', :body => ''))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEE::Connection.new('server.example.com', 'username', 'password')
#    lambda {
#      amee.get('/data')
#    }.should raise_error(AMEE::PermissionDenied,"You do not have permission to perform the requested operation")
#    amee.authenticated?.should be_true
#  end
#
#  it "should raise error if unhandled errors occur in connection" do
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '500', :body => ''))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEE::Connection.new('server.example.com', 'username', 'password')
#    lambda {
#      amee.get('/data')
#    }.should raise_error(AMEE::UnknownError,"An error occurred while talking to AMEE: HTTP response code 500")
#  end
#
#end
#
#describe AMEE::Connection, "with incorrect server name" do
#
#  it "should raise a useful error" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start).and_raise(SocketError.new)
#    amee = AMEE::Connection.new('badservername.example.com')
#    lambda{
#      amee.get('/')
#    }.should raise_error(AMEE::ConnectionFailed, "Connection failed. Check server name or network connection.")
#  end
#
#end
#
#describe AMEE::Connection, "with bad authentication information" do
#
#  it "should be capable of making requests for public URLs" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil, :request => flexmock(:code => '200', :body => ""), :finish => nil)
#    amee = AMEE::Connection.new('server.example.com', 'wrong', 'details')
#    lambda{amee.get('/')}.should_not raise_error
#  end
#
#  it "should get an authentication failure when accessing private URLs" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil, :request => flexmock(:code => '401', :body => "", :'[]' => nil), :finish => nil)
#    amee = AMEE::Connection.new('server.example.com', 'wrong', 'details')
#    lambda{amee.get('/data')}.should raise_error(AMEE::AuthFailed, "Authentication failed. Please check your username and password.")
#  end
#
#end
#
#describe AMEE::Connection, "without authentication" do
#
#  it "should not be capable of authentication" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil)
#    amee = AMEE::Connection.new('server.example.com')
#    amee.can_authenticate?.should be_false
#  end
#
#  it "should be capable of making requests for public URLs" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil, :request => flexmock(:code => '200', :body => ""), :finish => nil)
#    amee = AMEE::Connection.new('server.example.com')
#    amee.get('/') do |response|
#      response.should be_empty
#    end
#    amee.authenticated?.should be_false
#  end
#
#  it "should not be able to get private URLs" do
#    flexmock(Net::HTTP).new_instances.should_receive(:start => nil, :request => flexmock(:code => '401', :body => ""), :finish => nil)
#    amee = AMEE::Connection.new('server.example.com')
#    lambda{amee.get('/data')}.should raise_error(AMEE::AuthRequired, "Authentication required. Please provide your username and password.")
#  end
#
#  it "should be able to send post requests" do
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '200', :body => ''))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEE::Connection.new('server.example.com')
#    amee.post('/profiles', :test => 1, :test2 => 2) do |response|
#      response.should be_empty
#    end
#  end
#
#  it "should be able to send put requests" do
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '200', :body => ''))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEE::Connection.new('server.example.com')
#    amee.put('/profiles/ABC123', :test => 1, :test2 => 2) do |response|
#      response.should be_empty
#    end
#  end
#
#  it "should be able to send delete requests" do
#    flexmock(Net::HTTP).new_instances do |mock|
#      mock.should_receive(:start => nil)
#      mock.should_receive(:request).and_return(flexmock(:code => '200', :body => ''))
#      mock.should_receive(:finish => nil)
#    end
#    amee = AMEE::Connection.new('server.example.com')
#    amee.delete('/profiles/ABC123') do |response|
#      response.should be_empty
#    end
#  end
#
#end
