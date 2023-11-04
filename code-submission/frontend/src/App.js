import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import PreCancellation from "./routes/PreCancellation";
import PostCancellation from "./routes/PostCancellation";
export default function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<PreCancellation />} />
          <Route path="/post-cancellation" element={<PostCancellation />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
