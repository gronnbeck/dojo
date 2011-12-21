require File.dirname(__FILE__) + '/models.rb'
require 'httparty'
require 'hashie'

def update(playlist)
  playlist.clear
 
  mash = HTTParty.get("http://0.0.0.0:3000/playlists/1.json").parsed_response
  voted_list = mash[1]
  
  netlist = []
  voted_list.each do |voted|
    netlist << HTTParty.get("http://0.0.0.0:3000/tracks/#{voted["id"]}.json").parsed_response
  end
  
  netlist.each do |n|
    playlist.queue Spotify::Track.new(name:     n["name"], 
                                      href:     n["href"], 
                                      length:   n["length"].to_f)
  end
  puts "Playlist Updated #{Time.now}"
end

def started_playing(href)
  HTTParty.post("http://0.0.0.0:3000/playlists/remove/1/#{href}")
end

playlist = Spotify::PlayList.new

update(playlist)    
                    
while (!playlist.end)
  system "open #{playlist.current_track.href}"
  Thread.new do
    started_playing(playlist.current_track.href)
  end
  Thread.new do
    update(playlist)
  end
  sleep(playlist.current_track.length)

  playlist.next
end