fn is_prime(_number: i32) -> bool {
    true
}

fn main(){
    for i in 1..100{
        println!("{}: {}", i, is_prime(i))
    }
}
