import { useState } from 'react'
import ResultsDashboard from './compo/ResultsDashboard'

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    setLoading(true);
    const res = await fetch('http://localhost:8000/review', {
      method: 'POST',
      body: formData
    });
    const result = await res.json();
    setData(result);
    setLoading(false);
  };

  return (
    <div className="p-10 bg-slate-50 min-h-screen font-sans">
      <div className="max-w-2xl mx-auto bg-white p-8 rounded-xl shadow-md">
        <h1 className="text-3xl font-bold mb-6 text-center">AI Resume Reviewer</h1>

        <input
          type="file"
          onChange={handleUpload}
          className="block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        />

        {loading && <p className="mt-4 text-center animate-pulse">Analyzing...</p>}
        {data && <ResultsDashboard data={data} />}
      </div>
    </div>
  )
}

export default App