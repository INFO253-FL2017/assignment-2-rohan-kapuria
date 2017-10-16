var contactusform = document.getElementById("contactusform");
var commentForm = document.getElementById("commentForm");
contactusform.addEventListener("submit", function(event){
  event.preventDefault();
  var name = contactusform.elements.namedItem("nameinput").value;
  var subject = contactusform.elements.namedItem("subject").value;
  var comments = contactusform.elements.namedItem("comments").value;
  if ((name == "" ) || (name == null ) || (subject == "") || (subject == null) || (comments== "") ||(comments == null))
  {
    document.getElementById("submitmessage").innerHTML = "Please enter all fields!"
  } else
  {
    // var x = document.getElementById('form');
    // x.style.display = 'none';
    document.getElementById("contactusform").submit();
    // document.getElementById("submitmessage").innerHTML="Success! Your query has been submitted! You shall here back soon!"
  }
})
