import React, { useState, useEffect } from 'react';
import { api } from '../api';

function PatientHistory({ match }) {
  const [history, setHistory] = useState([]);
  const patientId = match?.params?.patientId || 1;

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const response = await api.get(`/patients/${patientId}/history`);
      setHistory(response.data);
    } catch (error) {
      console.error('Error fetching patient history:', error);
    }
  };

  return (
    <div>
      <h1>Patient History</h1>
      <ul>
        {history.length > 0 ? (
          history.map((record) => (
            <li key={record.id}>
              {record.date} - {record.doctor}: {record.report}
            </li>
          ))
        ) : (
          <p>No history found for this patient.</p>
        )}
      </ul>
    </div>
  );
}

export default PatientHistory;

