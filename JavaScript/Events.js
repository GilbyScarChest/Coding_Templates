// JQuery Syntax
//$(selector).on(event,childSelector,data,function,map)

// Form events
text.on("change", myFunction); // Fires the moment when the value of the element is changed
text.on("blur", myFunction); // Fires the moment that the element loses focus
text.on("contextmenu", myFunction); // Script to be run when a context menu is triggered
text.on("focus", myFunction); // Fires the moment when the element gets focus
text.on("input", myFunction); // Script to be run when an element gets user input
text.on("invalid", myFunction); // Script to be run when an element is invalid
text.on("reset", myFunction); // Fires when the Reset button in a form is clicked
text.on("search", myFunction); // Fires when the user writes something in a search field (for <input="search">)
text.on("select", myFunction); // Fires after some text has been selected in an element
text.on("submit", handleChange); // Fires when a form is submitted


// Mouse Events
button.on("click", myFunction); // Fires on a mouse click on the element
button.on("dblclick", myFunction); // Fires on a mouse double-click on the element
button.on("mousedown", myFunction); // Fires when a mouse button is pressed down on an element
button.on("mousemove", myFunction); // Fires when the mouse pointer is moving while it is over an element
button.on("mouseout", myFunction); // Fires when the mouse pointer moves out of an element
button.on("mouseover", myFunction); // Fires when the mouse pointer moves over an element
button.on("mouseup", myFunction); // Fires when a mouse button is released over an element
button.on("wheel", myFunction); // Fires when the mouse wheel rolls up or down over an element
button.on("scroll", myFunction); // Script to be run when an element's scrollbar is being scrolled

// Keyboard Events
textField.on("keydown", myFunction) // Fires when a user is pressing a key
textField.on("keypress", myFunction) // Fires when a user presses a key
textField.on("keyup", myFunction) // Fires when a user releases a key