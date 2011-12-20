require 'rss/1.0'
require 'rss/2.0'
require 'open-uri'

source = "http://feedproxy.google.com/typepad/alleyinsider/silicon_alley_insider"
content = ""
open(source) do |s| content = s.read end
rss = RSS::Parser.parse(content, false)

puts "Root values"
puts "RSS title: #{rss.channel.title}"
puts "RSS link: #{rss.channel.link}"
puts "RSS description: #{rss.channel.description}"
puts "RSS publication date #{rss.channel.date}"
puts ""
puts "Number of Items: #{rss.items.size}"
puts "All items in the RSS: "
for item in rss.items
  puts "#{item.title}" # - #{item.link}" 
  # other vars: link, description, date
end