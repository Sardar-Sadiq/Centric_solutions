import React from 'react';
import { CheckCircle, XCircle, AlertCircle } from 'lucide-react';
import { motion } from 'framer-motion';

const ResultsDashboard = ({ data }) => {
    if (!data) return null;

    const { score, found_keywords, missing_keywords } = data;

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="max-w-4xl mx-auto mt-10 p-8 bg-white rounded-2xl shadow-xl border border-gray-100"
        >
            <div className="flex items-center justify-between mb-8">
                <h2 className="text-2xl font-bold text-gray-800">Analysis Report</h2>
                <div className="text-right">
                    <span className="text-sm text-gray-500 uppercase tracking-wider font-semibold">Match Score</span>
                    <p className={`text-4xl font-black ${score > 70 ? 'text-green-500' : 'text-orange-500'}`}>
                        {score}%
                    </p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {/* Found Keywords */}
                <div className="space-y-4">
                    <h3 className="flex items-center text-lg font-semibold text-green-700">
                        <CheckCircle className="mr-2 w-5 h-5" /> Keywords Found
                    </h3>
                    <div className="flex flex-wrap gap-2">
                        {found_keywords.map((word) => (
                            <span key={word} className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-medium border border-green-200">
                                {word}
                            </span>
                        ))}
                    </div>
                </div>

                {/* Missing Keywords */}
                <div className="space-y-4">
                    <h3 className="flex items-center text-lg font-semibold text-red-700">
                        <XCircle className="mr-2 w-5 h-5" /> Missing Keywords
                    </h3>
                    <div className="flex flex-wrap gap-2">
                        {missing_keywords.map((word) => (
                            <span key={word} className="px-3 py-1 bg-red-100 text-red-700 rounded-full text-sm font-medium border border-red-200">
                                {word}
                            </span>
                        ))}
                    </div>
                </div>
            </div>

            {score < 50 && (
                <div className="mt-8 p-4 bg-amber-50 border-l-4 border-amber-400 flex items-start">
                    <AlertCircle className="text-amber-500 mr-3 mt-0.5" />
                    <p className="text-sm text-amber-800">
                        <strong>Tip:</strong> Your score is below 50%. Try adding more context about your experience with the missing keywords to pass ATS filters.
                    </p>
                </div>
            )}
        </motion.div>
    );
};

export default ResultsDashboard;