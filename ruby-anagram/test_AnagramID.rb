require 'kata_anagram.rb'

anagram_id = Kata::AnagramID.new('hello')

puts anagram_id.id
puts anagram_id.word
puts anagram_id.to_s