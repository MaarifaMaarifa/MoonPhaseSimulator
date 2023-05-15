use moon_phase_simulator::*;
use std::io::{self, Write};

fn main() {
    let mut input = String::new();

    print!("Enter number of days since new moon phase: ");
    io::stdout().flush().expect("failed to flush stdout");

    io::stdin()
        .read_line(&mut input)
        .expect("failed to get user input");

    let days = input.trim().parse::<f64>().unwrap_or_else(|err| {
        eprintln!("Error: {}", err);
        std::process::exit(1);
    });

    let moon = Moon::from_days_after_new_moon(days);

    println!("The moon phase is {:?}", moon.get_phase());
}
