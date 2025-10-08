// Toast component functionality
function showToast(title, message, type = 'success') {
    const toastComponent = document.getElementById('toast-component');
    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');

    if (!toastComponent) {
        console.error('Toast component not found');
        return;
    }

    // Set content
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Set icon and colors based on type
    const types = {
        success: {
            icon: '✓',
            bg: 'bg-white',           
            border: 'border-white-500',
            text: 'text-green-800'
        },
        error: {
            icon: '✕',
            bg: 'bg-white',         
            border: 'border-red-500',
            text: 'text-red-800'
        },
        warning: {
            icon: '⚠',
            bg: 'bg-white',           
            border: 'border-yellow-500',
            text: 'text-yellow-800'
        },
        info: {
            icon: 'ℹ',
            bg: 'bg-white',          
            border: 'border-blue-500',
            text: 'text-blue-800'
        }
    };

    const style = types[type] || types.success;
    
    toastIcon.textContent = style.icon;
    
    // Remove all previous color classes
    toastComponent.className = `fixed bottom-8 right-8 p-4 px-8 rounded-xl shadow-xl z-50 transition-all duration-300 flex items-center gap-4 border-l-4 ${style.bg} ${style.border}`;
    toastTitle.className = `font-bold ${style.text}`;
    toastMessage.className = `text-gray-700 text-sm line-clamp-3`;

    // Show toast
    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Hide after 5 seconds
    setTimeout(() => {
        hideToast();
    }, 5000);
}

function hideToast() {
    const toastComponent = document.getElementById('toast-component');
    if (toastComponent) {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }
}

// Initialize logout handlers
function initLogoutHandlers() {
    // Find ALL logout links (both desktop and mobile)
    const logoutLinks = document.querySelectorAll('a[href*="logout"]');
    
    console.log('Found logout links:', logoutLinks.length); // Debug log
    
    logoutLinks.forEach(function(logoutLink) {
        // Remove any existing listeners to avoid duplicates
        logoutLink.replaceWith(logoutLink.cloneNode(true));
    });
    
    // Re-select after cloning
    const freshLogoutLinks = document.querySelectorAll('a[href*="logout"]');
    
    freshLogoutLinks.forEach(function(logoutLink) {
        logoutLink.addEventListener('click', async function(e) {
            e.preventDefault();
            
            const logoutUrl = this.href;
            console.log('Logout clicked, URL:', logoutUrl); // Debug log
            
            try {
                const response = await fetch(logoutUrl, {
                    method: 'GET',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });
                
                console.log('Response status:', response.status); // Debug log
                
                const data = await response.json();
                console.log('Response data:', data); // Debug log
                
                if (data.success) {
                    // Show toast notification
                    showToast('Logged Out', data.message, 'success');
                    
                    // Redirect after showing toast
                    setTimeout(() => {
                        window.location.href = data.redirect;
                    }, 1500);
                } else {
                    showToast('Error', 'Logout failed', 'error');
                }
            } catch (error) {
                console.error('Logout error:', error);
                // Fallback: redirect normally if AJAX fails
                showToast('Error', 'Logout failed, redirecting...', 'error');
                setTimeout(() => {
                    window.location.href = logoutUrl;
                }, 1000);
            }
        });
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLogoutHandlers);
} else {
    // DOM is already ready
    initLogoutHandlers();
}

// Re-initialize after any dynamic content loads (for mobile menu)
document.addEventListener('click', function(e) {
    if (e.target.id === 'mobile-menu-toggle') {
        setTimeout(initLogoutHandlers, 100);
    }
});

// Make showToast available globally
window.showToast = showToast;
window.hideToast = hideToast;