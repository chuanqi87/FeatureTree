import React from "react";
import { createRoot } from "react-dom/client";
import { Button, Result } from "antd";
import App from "./app/App.jsx";
import "antd/dist/reset.css";
import "./app/styles.css";

class ErrorBoundary extends React.Component {
  state = { error: null };
  static getDerivedStateFromError(error) {
    return { error };
  }
  render() {
    return this.state.error ? (
      <Result
        status="error"
        title="页面加载失败"
        subTitle={this.state.error.message}
        extra={
          <Button type="primary" onClick={() => window.location.reload()}>
            重新加载
          </Button>
        }
      />
    ) : (
      this.props.children
    );
  }
}

createRoot(document.getElementById("root")).render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
);
