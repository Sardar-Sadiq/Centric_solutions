import React from 'react';
import { CheckCircle, XCircle, AlertCircle } from 'lucide-react';
import { motion } from 'framer-motion';

const ResultsDashboard = ({ data }) => {
    // 1. Safety Check: If the API hasn't returned data yet, don't render.
    if (!data) return null;

    // 2. Destructuring: Match these exactly with your backend keys.
    // We provide empty arrays [] as defaults to prevent .map() from crashing.
    const { score = 0, found = [], missing = [] } = data;

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="max-w-4xl mx-auto mt-10 p-8 bg-white rounded-2xl shadow-xl border border-gray-100"
        >
            <div className="flex items-center justify-between mb-8">
                <h2 className="text-2xl font-bold text-gray-800">Analysis Report</h2>
                <div className="text-right">
                    <span className="text-sm text-gray-500 uppercase tracking-wider font-semibold text-slate-400">Match Score</span>
                    <p className={`text-4xl font-black ${score > 70 ? 'text-green-500' : 'text-orange-500'}`}>
                        {score}%
                    </p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {/* Found Keywords Section */}
                <div className="space-y-4">
                    <h3 className="flex items-center text-lg font-semibold text-green-700">
                        <CheckCircle className="mr-2 w-5 h-5" /> Keywords Found
                    </h3>
                    <div className="flex flex-wrap gap-2">
                        {/* Corrected: using 'found' instead of 'found_keywords' */}
                        {found.length > 0 ? (
                            found.map((word, index) => (
                                <span key={index} className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-medium border border-green-200">
                                    {word}
                                </span>
                            ))
                        ) : (
                            <span className="text-slate-400 text-sm italic">No matching keywords found.</span>
                        )}
                    </div>
                </div>

                {/* Missing Keywords Section */}
                <div className="space-y-4">
                    <h3 className="flex items-center text-lg font-semibold text-red-700">
                        <XCircle className="mr-2 w-5 h-5" /> Missing Keywords
                    </h3>
                    <div className="flex flex-wrap gap-2">
                        {/* Corrected: using 'missing' instead of 'missing_keywords' */}
                        {missing.length > 0 ? (
                            missing.map((word, index) => (
                                <span key={index} className="px-3 py-1 bg-red-100 text-red-700 rounded-full text-sm font-medium border border-red-200">
                                    {word}
                                </span>
                            ))
                        ) : (
                            <span className="text-slate-400 text-sm italic">Perfect! No missing keywords.</span>
                        )}
                    </div>
                </div>
            </div>

            {/* Dynamic Advice based on score */}
            {score < 50 && (
                <div className="mt-8 p-4 bg-amber-50 border-l-4 border-amber-400 flex items-start">
                    <AlertCircle className="text-amber-500 mr-3 mt-0.5 shrink-0" />
                    <p className="text-sm text-amber-800">
                        <strong>Mentor Tip:</strong> Your score is below 50%. This usually means your resume is missing specific technical terms the ATS is looking for. Consider tailoring your "Skills" section!
                    </p>
                </div>
            )}
        </motion.div>
    );
};

export default ResultsDashboard;