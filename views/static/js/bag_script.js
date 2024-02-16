document.addEventListener("DOMContentLoaded", function() {
    const decreaseBtn = document.getElementById('decrease_btn');
    const increaseBtn = document.getElementById('increase_btn');
    const quantityElement = document.querySelector('.quantity');
    const resetBtn = document.getElementById('reset_btn');

    let quantity = 1;

    function updateQuantityDisplay() {
        quantityElement.textContent = quantity;
    }

    function increaseQuantity() {
        quantity++;
        updateQuantityDisplay();
    }

    function decreaseQuantity() {
        if (quantity > 1) {
            quantity--;
            updateQuantityDisplay();
        }
    }

    function resetQuantity() {
        quantity = 1;
        updateQuantityDisplay();
    }

    increaseBtn.addEventListener('click', increaseQuantity);
    decreaseBtn.addEventListener('click', decreaseQuantity);
    resetBtn.addEventListener('click', resetQuantity);
});