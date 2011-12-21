require 'hashie'
require 'httparty'

puts "What you wanna search for?"
search_for = gets.chomp

search_for = search_for.strip.sub(/ /, '%20')

mash = Hashie::Mash.new HTTParty.get("http://ws.spotify.com/search/1/track?q=#{search_for}")

tracks = mash.tracks.track

puts "\nTracks found for #{search_for}"
tracks.each do |track|
  puts "#{tracks.index(track) + 1}. #{track.name}"
end

puts "\nWhich track do you want to play? (Enter number)"
chosen_track = gets
chosen_track = chosen_track.to_i

puts "Start playing #{tracks[chosen_track - 1].name}"
system "open #{tracks[chosen_track - 1].href}"



