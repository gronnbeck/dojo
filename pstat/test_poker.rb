require "./poker.rb"
require "test/unit"

class TestCard < Test::Unit::TestCase
	def test_init_with_valid_parameters
		c = Card.new("H",2)
		assert_equal("H", c.face)
		assert_equal(2, c.value)
	end

	def test_init_with_invalid_value
		assert_raise ArgumentError do
			Card.new("H", 14)
			Card.new("H", 0)
			Card.new("H", -1)
		end
	end

	def test_init_with_invalid_face
		assert_raise ArgumentError do
			Card.new("G", 10)
			Card.new(10,10)
			Card.new(-2, 10)
		end
	end

	def test_comparable
		assert Card.new("S", 10) > Card.new("S", 9)
	end
end

class TestDeck < Test::Unit::TestCase
	def test_deck_size
		assert_equal 52, Deck.new.size, "A fresh deck should be of 52 cards"
	end
end

class TestPokerRank < Test::Unit::TestCase
	def test_self_flush 
		assert_equal true, PokerRank.flush?([Card.new("H",10), Card.new("H", 7)])
	end

	def test_self_straigth
		assert_equal true, PokerRank.straigth?([Card.new("S", 1), Card.new("S", 2), 
			Card.new("S", 3)])
	end

	def test_self_pair
		assert_equal true, PokerRank.pair?([Card.new("S", 2), Card.new("S", 4),
			Card.new("D", 2)])
	end

	def test_two_pairs
		assert_equal true, PokerRank.two_pairs?([Card.new("S",2), Card.new("S",3),
			Card.new("D",2), Card.new("D",3)])
	end

	def test_house
		assert PokerRank.house?([Card.new("S", 2), Card.new("D", 2),
			Card.new("S", 3), Card.new("D", 3), Card.new("H", 3)])
	end 
end
