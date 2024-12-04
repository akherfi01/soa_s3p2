import React, { useState, useEffect } from 'react';
import { api } from '../api';

function PatientHistory({ match }) {
  const [history, setHistory] = useState([]);
  const patientId = match.params.patientId;

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await api.get(`/patients/${patientId}/history`);
        setHistory(response.data);
      } catch (err) {
        console.error('Error fetching patient history:', err);
      }
    };

    fetchHistory();
  }, [patientId]);

  return (
    <div>
      <h1>Patient History</h1>
      {history.length ? (
        <ul>
          {history.map((record) => (
            <li key={record.id}>
              <strong>Date:</strong> {record.date}, <strong>Doctor:</strong> {record.doctor}, <strong>Report:</strong> {record.report}
            </li>
          ))}
        </ul>
      ) : (
        <p>No history found for this patient.</p>
      )}
    </div>
  );
}

export default PatientHistory;

