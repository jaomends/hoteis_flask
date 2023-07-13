import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';

const columns = [
  { field: "id", headerName: 'ID', width: 200 },
  { field: "id_design_diploma", headerName: 'ID Design Diploma', width: 200 },
  { field: "files_design", headerName: 'Files Design', width: 200 },
];

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/design/files');
      const transformedData = response.data.files_design.map((item, index) => ({
        id: index + 1,
        id_design_diploma: item.id_design_diploma,
        files_design: item.files_design
      }));
      setData(transformedData);
    } catch (error) {
      console.log(error);
    }
  };
  
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid rows={data} columns={columns} pageSize={5} 
        checkboxSelection
      />
    </div>
  );
}

export default App;

