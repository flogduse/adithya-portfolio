import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Relative base keeps dist/index.html portable (works from any static host or subpath)
export default defineConfig({
  base: './',
  plugins: [react()],
  // Keep dist output tidy
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false
  }
});
