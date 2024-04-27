 // Check for access token and user information in localStorage
 const accessToken = localStorage.getItem("access_token");

 // Redirect to login if no access token or user information
 if (!accessToken ) {
 window.location.href = "{% url 'login' %}";
 return; // Exit the function if redirected
 }