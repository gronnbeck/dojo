require File.dirname(__FILE__).to_s + '/models.rb'  
require 'test/unit'

class TestModels < Test::Unit::TestCase
  def setup
    @track = Spotify::Track.new(name: "track name", 
                                href: "test", 
                                length: 35, 
                                artist: {name: 'artist'})
                                
    @track2 = Spotify::Track.new(name: "track name", 
                                 href: "test", 
                                 length: 35, 
                                 artist: {name: 'artist'})
  end
  
  def test_initialization_of_track
    
    assert_not_nil(@track.name)
    assert_not_nil(@track.href)
    assert_not_nil(@track.length)
    assert_not_nil(@track.artist)
    
    assert_equal("track name", @track.name)
    assert_equal("test", @track.href)
    assert_equal(35, @track.length)
    assert_equal({name: 'artist'}, @track.artist)
  end
  
  def test_initialization_of_artist
    artist = Spotify::Artist.new("artist name", "href", {track: 'one_track'})
    assert_equal("artist name", artist.name)
    assert_equal("href", artist.href)
    assert_equal({track: 'one_track'}, artist.tracks)
  end
  
  def test_player
    plist = Spotify::PlayList.new
    assert_not_nil plist, "Playlist shouldn't be nil"
    
    plist.queue(@track)
    assert_equal 1, plist.size, "The playlist should have contained 1 track"
    

    plist.queue(@track2)
    assert_equal 2, plist.size, "The playlist should have contained 2 track"    
  end
  

end
