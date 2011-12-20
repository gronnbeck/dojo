module Kata
  class AnagramID
    def initialize(word)
      @@id = array_to_string word.downcase.strip.scan(/./).sort
      @@word = word.downcase
    end
  
    def id
      @@id
    end
  
    def word
      @@word
    end
  
    def to_s
      "(#{@@id}, #{@@word})"
    end
  
    :private
    def array_to_string(array)
      string = ""
      for item in array
        string = string + item.to_s
      end 
      string
    end
  end
  
  def anagram_hash(word_list)
    hash = Hash.new
    for word in word_list
     list_item = AnagramID.new(word)
     if hash[list_item.id] == nil
       hash[list_item.id] = [list_item.word] 
     else
       hash[list_item.id].push list_item.word
     end
    end
    hash
  end
end