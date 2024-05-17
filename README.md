Here is my task on password complexity checker,
Added special character criteria: The criteria dictionary now includes a check for special characters (!@#$%^&*()) to encourage stronger passwords.
Increased maximum score: The complexity_score can now reach 5 if all criteria are met.
Handled invalid passwords: The assess_password_strength function now returns "invalid password" if none of the criteria are met.
Improved error handling: The assess_password_strength function uses get with a default value to handle unexpected complexity scores.
