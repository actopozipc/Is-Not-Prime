fn is_not_prime(_number: i32) -> bool {
    true
}

fn main(){
    for i in 1..100{
        println!("{}: {}", i, is_not_prime(i))
    }
}
