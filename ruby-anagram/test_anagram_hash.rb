require 'kata_anagram.rb'
include Kata

wordlist = ["hello", "ehllo", "hlloe", "2pac" ]

hash = anagram_hash(wordlist)

hash.each_key do |key|
  puts key
end