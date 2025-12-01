use std::collections::HashMap;

struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

impl User {
    fn new(username: String, email: String) -> User {
        User {
            username,
            email,
            sign_in_count: 1,
            active: true,
        }
    }

    fn deactivate(&mut self) {
        self.active = false;
        println!("User {} has been deactivated.", self.username);
    }
}

fn main() {
    let mut users = HashMap::new();
    let user1 = User::new(String::from("rust_fan"), String::from("rust@example.com"));
    
    users.insert("u1", user1);

    match users.get_mut("u1") {
        Some(u) => u.deactivate(),
        None => println!("User not found"),
    }
}