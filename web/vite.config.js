import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  build: { rolldownOptions: { output: { codeSplitting: {
    groups: [{ name: "react", test: /node_modules\/(?:react|react-dom|scheduler)\//, includeDependenciesRecursively: false }],
  } } } },
  plugins: [react()],
  server: { proxy: { "/api": "http://127.0.0.1:8765" } },
});
