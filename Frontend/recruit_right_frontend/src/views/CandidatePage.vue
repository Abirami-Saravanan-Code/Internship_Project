<template>
    <div>
      <h1>Welcome, Candidate</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CandidatePage',
  };
  </script>
  

  john = User.objects.create(
    name="John",
    email="john@example.com",
    role="Hiring Manager"
)

print(f"User {john.name} created with role {john.role}")