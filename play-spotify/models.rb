require 'hashie'
require 'httparty'

module Spotify
  class Track
    attr_accessor :name, :href, :length, :artist
    def initialize(args)
      @name = args[:name]
      @href = args[:href]
      @length = args[:length]
      @artist = args[:artist]
    end    
  end
  
  class Artist
    attr_accessor :name, :href, :tracks
    def initialize(name, href, tracks)
      @name = name
      @href = href
      @tracks = tracks
    end
  end
  
  class PlayList
    def initialize
      @playlist = []
      @current = -1
    end
    
    def next
      @current = @current + 1 
    end
    
    def prev
      @current = @current - 1
    end
    
    def current_track
      @playlist[@current]
    end
    
    def queue(track)
      @current = 0 if @current == -1
      @playlist << track
    end
    
    def clear 
      playlist = []
      @current = -1
    end
    
    def size
      @playlist.size
    end
    
    def end
      @current >= size
    end
    
  end
end