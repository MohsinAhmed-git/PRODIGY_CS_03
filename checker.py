def password_complexity(password):
  """
  This function defines criteria for password complexity and counts the number of met criteria.

  Args:
      password: The password to be evaluated.

  Returns:
      An integer representing the number of complexity criteria met (0-5).
  """
  criteria = {
      'length': len(password) >= 8,
      'uppercase': any(char.isupper() for char in password),
      'lowercase': any(char.islower() for char in password),
      'digit': any(char.isdigit() for char in password),
      'special': any(char in "!@#$%^&*()" for char in password)  # Add special character criteria
  }

  # Count the number of met criteria
  complexity_score = sum(criteria.values())

  return complexity_score

def assess_password_strength(complexity_score):
  """
  This function assesses password strength based on the complexity score.

  Args:
      complexity_score: The number of complexity criteria met (0-5).

  Returns:
      A string representing the password strength ("very weak" to "very strong").
  """
  strength_map = {
      5: "very strong",
      4: "strong",
      3: "moderate",
      2: "weak",
      1: "very weak",
      0: "invalid password"  # Handle passwords that don't meet any criteria
  }

  return strength_map.get(complexity_score, "invalid score")  # Handle invalid complexity scores

# Example usage
password = "Mohsin Ahmed@12"
complexity_score = password_complexity(password)
strength = assess_password_strength(complexity_score)
print(f"The password '{password}' is {strength}.")
