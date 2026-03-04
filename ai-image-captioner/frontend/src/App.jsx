import React, { useState } from 'react';
import { Upload, Image as ImageIcon, Sparkles, RefreshCw } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [caption, setCaption] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
      setCaption(""); // Reset caption for new image
    }
  };

  const generateCaption = async () => {
    if (!file) return;

    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/caption', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Backend error');

      const data = await response.json();
      setCaption(data.caption);
    } catch (error) {
      console.error("Error:", error);
      setCaption("Failed to generate caption. Is the Python server running?");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-black">

      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-10"
      >
        <h1 className="text-4xl  font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 mb-2">
          AI image captioner
        </h1>
        <p className="text-slate-400">Transform pixels into poetry with neural captioning.</p>
      </motion.div>

      <div className="w-full max-w-2xl bg-slate-900/50 backdrop-blur-xl border border-slate-800 p-8 rounded-3xl shadow-2xl">

        {/* Upload/Preview Section */}
        <div className="relative group rounded-2xl border-2 border-dashed border-slate-700 hover:border-blue-500/50 transition-colors overflow-hidden bg-slate-950/50">
          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
          />

          {preview ? (
            <img src={preview} alt="Upload preview" className="w-full h-64 object-contain p-2" />
          ) : (
            <div className="h-64 flex flex-col items-center justify-center space-y-4">
              <div className="p-4 bg-slate-900 rounded-full text-blue-400 group-hover:scale-110 transition-transform">
                <Upload size={32} />
              </div>
              <p className="text-slate-500 font-medium">Click or drag image to begin</p>
            </div>
          )}
        </div>

        {/* Controls */}
        <div className="mt-8 flex flex-col items-center space-y-6">
          <button
            onClick={generateCaption}
            disabled={!file || isLoading}
            className="group relative px-8 py-3 bg-blue-600 hover:bg-blue-500 disabled:bg-slate-800 disabled:text-slate-500 text-white font-bold rounded-xl transition-all flex items-center gap-2 overflow-hidden"
          >
            {isLoading ? (
              <RefreshCw className="animate-spin" size={20} />
            ) : (
              <Sparkles className="group-hover:rotate-12 transition-transform" size={20} />
            )}
            <span>{isLoading ? "Analyzing Patterns..." : "Generate Caption"}</span>
          </button>

          {/* Result Area */}
          <AnimatePresence>
            {caption && (
              <motion.div
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0 }}
                className="w-full p-6 bg-slate-800/50 border border-blue-500/30 rounded-2xl"
              >
                <div className="flex items-center gap-2 text-blue-400 mb-2 text-sm font-bold uppercase tracking-widest">
                  <ImageIcon size={16} />
                  AI Vision Result
                </div>
                <p className="text-xl text-slate-100 italic leading-relaxed">
                  "{caption}"
                </p>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>

      <footer className="mt-12 text-slate-600 text-sm">
        Built with Bun + FastAPI + Transformers
      </footer>
    </div>
  );
}

export default App;