import os from "node:os"
import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

const apiProxyTarget =
  process.env.E2E_API_URL ??
  process.env.VITE_API_PROXY_TARGET ??
  "http://127.0.0.1:8000"

// https://vite.dev/config/
export default defineConfig({
  base: './',
  cacheDir: path.join(os.tmpdir(), 'course30daysv2-vite-cache'),
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      '/api': apiProxyTarget,
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes('node_modules')) {
            return undefined;
          }

          if (id.includes('recharts') || id.includes('d3-')) {
            return 'vendor-charts';
          }

          if (id.includes('react-markdown') || id.includes('remark-') || id.includes('rehype-') || id.includes('katex') || id.includes('mdast') || id.includes('unist')) {
            return 'vendor-richtext';
          }

          if (id.includes('@radix-ui') || id.includes('cmdk') || id.includes('vaul')) {
            return 'vendor-ui';
          }

          return undefined;
        },
      },
    },
  },
});
