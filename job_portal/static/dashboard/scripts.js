class Dashboard {
    constructor() {
        this.initializeElements();
        this.initializeState();
        this.bindEvents();
        this.loadSavedPreferences();
    }
    
    initializeElements() {
        this.elements = {
            sidebar: document.getElementById('sidebar'),
            mainContent: document.getElementById('mainContent'),
            sidebarCollapseBtn: document.getElementById('sidebarCollapseBtn'),
            themeToggleBtn: document.getElementById('themeToggleBtn'),
            sidebarOverlay: document.getElementById('sidebarOverlay'),
            fullscreenBtn: document.getElementById('fullscreenBtn'),
            themeIcon: document.getElementById('themeIcon'),
            fullscreenIcon: document.getElementById('fullscreenIcon')
        };
    }
    
    initializeState() {
        this.state = {
            sidebarCollapsed: false,
            isMobile: window.innerWidth <= 992,
            isFullscreen: false,
            theme: 'light'
        };
    }
    
    bindEvents() {
        // Sidebar events
        this.elements.sidebarCollapseBtn?.addEventListener('click', () => this.toggleSidebar());
        this.elements.sidebarOverlay?.addEventListener('click', () => this.closeMobileSidebar());
        
        // Theme toggle
        this.elements.themeToggleBtn?.addEventListener('click', () => this.toggleTheme());
        
        // Fullscreen toggle
        this.elements.fullscreenBtn?.addEventListener('click', () => this.toggleFullscreen());
        
        // Window events
        window.addEventListener('resize', () => this.handleResize());
        document.addEventListener('fullscreenchange', () => this.handleFullscreenChange());
    }
    
    toggleSidebar() {
        if (this.state.isMobile) {
            this.toggleMobileSidebar();
        } else {
            this.toggleDesktopSidebar();
        }
    }
    
    toggleDesktopSidebar() {
        this.state.sidebarCollapsed = !this.state.sidebarCollapsed;
        this.elements.sidebar.classList.toggle('collapsed', this.state.sidebarCollapsed);

        // Toggle rotation manually
        this.elements.sidebarCollapseBtn.querySelector('.collapse-icon')?.classList.toggle('rotated', this.state.sidebarCollapsed);

        this.saveSidebarState();
    }
    
    toggleMobileSidebar() {
        const isOpen = this.elements.sidebar.classList.contains('show');
        if (isOpen) {
            this.closeMobileSidebar();
        } else {
            this.openMobileSidebar();
        }
    }
    
    openMobileSidebar() {
        this.elements.sidebar.classList.add('show');
        this.elements.sidebarOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    
    closeMobileSidebar() {
        this.elements.sidebar.classList.remove('show');
        this.elements.sidebarOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }
    
    toggleTheme() {
        this.state.theme = this.state.theme === 'light' ? 'dark' : 'light';
        this.applyTheme();
        this.saveTheme();
    }
    
    applyTheme() {
        document.documentElement.setAttribute('data-bs-theme', this.state.theme);
        const iconClass = this.state.theme === 'dark' ? 'bi-sun' : 'bi-moon';
        this.elements.themeIcon.className = `bi ${iconClass}`;
    }
    
    toggleFullscreen() {
        if (!this.state.isFullscreen) {
            this.enterFullscreen();
        } else {
            this.exitFullscreen();
        }
    }
    
    enterFullscreen() {
        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen()
                .catch(err => console.warn('Fullscreen failed:', err));
        }
    }
    
    exitFullscreen() {
        if (document.exitFullscreen) {
            document.exitFullscreen()
                .catch(err => console.warn('Exit fullscreen failed:', err));
        }
    }
    
    handleFullscreenChange() {
        this.state.isFullscreen = !!document.fullscreenElement;
        const iconClass = this.state.isFullscreen ? 'bi-fullscreen-exit' : 'bi-fullscreen';
        this.elements.fullscreenIcon.className = `bi ${iconClass}`;
    }
    
    handleResize() {
        const wasMobile = this.state.isMobile;
        this.state.isMobile = window.innerWidth <= 992;
        
        if (wasMobile !== this.state.isMobile) {
            this.closeMobileSidebar();
            if (!this.state.isMobile) {
                this.elements.sidebar.classList.toggle('collapsed', this.state.sidebarCollapsed);
            }
        }
    }
    
    loadSavedPreferences() {
        this.loadTheme();
        this.loadSidebarState();
    }
    
    loadTheme() {
        try {
            const savedTheme = localStorage.getItem('theme');
            this.state.theme = savedTheme === 'dark' ? 'dark' : 'light'; // fallback to light
        } catch (error) {
            console.warn('Could not load theme from localStorage:', error);
            this.state.theme = 'light';
        }
        this.applyTheme();
    }
    
    loadSidebarState() {
        // Default to not collapsed
        this.state.sidebarCollapsed = false;
        if (!this.state.isMobile) {
            this.elements.sidebar.classList.toggle('collapsed', this.state.sidebarCollapsed);
        }
    }
    saveTheme() {
        try {
            localStorage.setItem('theme', this.state.theme);
        } catch (error) {
            console.warn('Could not save theme to localStorage:', error);
        }
    }
    
    saveSidebarState() {
        // Sidebar state would be saved here if localStorage was available
        console.log('Sidebar state saved:', this.state.sidebarCollapsed);
    }
}

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.dashboard = new Dashboard();
});