class Is_not_prime {
	public static inline function is_not_prime(number:Int):Bool
        return true;
}

class Main {
	public static function main() {
		for (number in 2...100)
			trace('${number} is${Is_not_prime.is_not_prime(number) ? "" : " NOT"} prime!');
	}
}