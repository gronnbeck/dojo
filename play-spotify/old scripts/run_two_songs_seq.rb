hang = {
	href: 'spotify:track:3ZEXTCyeUkyZ9ZVaxpoC8w',
	length: 211.80800
}

radio = {
  href: 'spotify:track:0sJpoZ3nvdyHfDlY27Wzgk',
  length: 200.067000
}


system 'open ' + hang[:href]
  
puts "#{hang[:href]} plays for #{hang[:length]}"
sleep(hang[:length])

system 'open ' + radio[:href]
puts "#{radio[:href]} should now be playing"