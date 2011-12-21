module Spotify
  class Search
    def self.track(track_name)
      mash_of_tracks = \
        get_mash_of("http://ws.spotify.com/search/1/track?q=#{track_name}").tracks.track
      tracks = []
      mash_of_tracks.each do |track|
        tracks << Track.new(track.name, track.href, track.length, track.artist)
      end
    end
    
    def self.artist(artist_name)
      mash_of_artists = \
        get_mash_of("http://ws.spotify.com/search/1/artist?q=#{artist_name}").artist.artist
      artists = []
      mash_of_artists.each do |artist|
#        artists << Artist.new(DONT KNOW THE PARAMETERS)
      end
    end
    
    private
    
    def self.get_mash_of(url)
      Hashie::Mash.new HTTParty.get(clean(url))
    end
    
    def self.clean(input)
      input.strip.sub(/ /, '%20')
    end
  end
end

class TestSearch < Test::Unit::TestCase  
  def test_search_for_tracks
    tracks = Spotify::Search.track("fix you")
    assert_not_nil(tracks)
    assert tracks.instance_of? Array
  end
end