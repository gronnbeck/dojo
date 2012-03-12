
class Card
	include Comparable
	attr_accessor :value, :face

	def <=>(other)
		@value <=> other.value		
	end

	def initialize(face, value)
		self.value = value
		self.face = face
	end

	@@valid_faces = { "H" => true, "S" => true, "D" => true, "C" => true }
	def self.valid_faces
		@@valid_faces
	end
	
	def valid_face?(face)
		face.instance_of? String and @@valid_faces.has_key? face.upcase
	end

	@@value_map = { "A" => 1, "J" => 11, "K" => 13, "Q" => 12 }
	def valid_value?(value)	
		value_mapped? value or (1 <= value and value <= 13) 	
	end

	def value_mapped?(value)
		value.instance_of? String and @@value_map.has_key? value.upcase
	end
	
	private
	def value=(value)
		if not valid_value?(value)
			raise ArgumentError,
					"Invalid card value: Should be an integer from 1-13, or A, J, Q, K"
		elsif value_mapped?(value) 
			@value = value_map(value)
		else
			@value = value
		end
	end

	def face=(face)
		if not valid_face?(face)
			raise ArgumentError, 
					"Invalid face value: Should be either H, S, D, or C"
		else
			@face = face
		end
	end
	
end

class Deck
	def initialize
		@deck = []
		(1..13).each do |value|
			Card.valid_faces.each_key do |face|
				@deck << Card.new(face, value)
			end
		end
	end

	def size
		@deck.size
	end

	def get(index)
		@deck[index]
	end

	def each
		@deck.each
	end
end

class PokerRank
	def self.flush(cards)
		kind = cards[0].face
		cards.reduce(true) do |bool, val|
			return nil if not val
			bool and val.face == kind
		end
		cards.max
	end

	def self.flush?(cards)
		not nil == flush(cards)
	end

	def self.straigth(cards)
		cards.sort.reduce(0) do |prev, val|
			 if not prev < val.value
				return nil
			end
			val.value
		end
		cards.max
	end

	def self.straigth?(cards)
		not nil == straigth(cards)
	end
	
	def self.of_a_kind(cards, n)
		compare = {}
		cards.each do |card|
			if compare.has_key?(card.value)
				compare[card.value] = compare[card.value] + 1
				return card if compare[card.value] == n
			else
				compare[card.value] = 1
			end
		end
		return nil
	end

	def self.pair(cards)
		of_a_kind(cards, 2)
	end

	def self.pair?(cards)
		not nil == pair(cards)
	end

	def self.clone(cards)
		cards = cards.clone.map do |c| c.clone end 
	end

	def self.pop(card_value, cards)
		cards.each do |c|
			cards.delete(c) if c.value == card_value
		end
	end

	def self.two_pairs(cards)
		clone(cards)
		pair = pair(cards)
		cards = pop(pair.value, cards)
		[pair, pair(cards)]
	end

	def self.two_pairs?(cards)
		two_pairs(cards).reduce(true) do |bool, val|
			bool and not nil
		end
	end

	def self.house?(cards)
		clone(cards) 
		pair = self.pair(cards)
		return false if pair.nil?
		cards = pop(pair.value, cards)
		true if of_a_kind(cards, 3)
	end

	def self.straigth_flush?(cards)
		straight? cards and flush? cards
	end

end

module Holdem
	class Hand
		attr_accessor :hand
		def initialize(card1, card2)
			@hand = [card1, card2]
		end
	end

	class HandStat

		def initialize(hand)
			@hand = hand
		end

		def blind
			
		end
	end
end





