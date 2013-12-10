 def tokenize(string)

	(0..string.length).each do |i|
		puts string
		string.gsub! '(', '( '
		string.gsub! ')', ' )'
	end

	return string.split
end

def parse(string)
	def parse_tokens(tokens, inner)
		res = []
		while tokens.length > 0 do
			current = tokens.pop(0)
			if current == '('
				res.append(parse_tokens(tokens, True))
			end

		end

	end

end