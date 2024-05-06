document.addEventListener('DOMContentLoaded', function() {
    
    // Function to validate the sentence input
    function validateInput() {
        const sentenceInput = document.getElementById('sentenceInput');
        if (sentenceInput.value.trim() === '') {
            alert('Please enter a sentence to generate the parse tree.');
            return false;
        }
        return true;
    }
    
    // Function to display a loading message
    function displayLoading(isLoading) {
        const loadingText = document.getElementById('loadingText');
        if (isLoading) {
            loadingText.style.display = 'block'; // Show loading text
        } else {
            loadingText.style.display = 'none';  // Hide loading text
        }
    }
    
    // Event listener for form submission
    const form = document.querySelector('form');
    form.onsubmit = function(e) {
        e.preventDefault();  // Prevent form from submitting normally
        
        if (!validateInput()) {
            return; // Stop the function if the input is not valid
        }
        
        displayLoading(true); // Show loading message

        // Perform AJAX request to generate the tree
        const xhr = new XMLHttpRequest();
        const formData = new FormData(form);
        xhr.open('POST', '/generate_tree', true);
        
        // Handle the response from the server
        xhr.onload = function () {
            if (this.status == 200) {
                const response = JSON.parse(this.responseText);
                const parseTreeImage = document.getElementById('parseTreeImage');
                
                // Update the src attribute of the image to display the new parse tree
                parseTreeImage.src = response.treeImageUrl;
                
                displayLoading(false); // Hide loading message
            } else {
                alert('There was an error generating the parse tree.');
                displayLoading(false);
            }
        };

        // Send the form data to the server
        xhr.send(formData);
    };
    
    // Add additional JavaScript enhancements below as needed
});
