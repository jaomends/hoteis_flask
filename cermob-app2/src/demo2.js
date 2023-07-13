import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';

const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'fileName', headerName: 'First name', width: 130 },
];

const rows = [
    { id: 'sakndsa', fileName: 'files_design'},
    { id: 'dsadadasadsas', fileName: 'files_design'},
];

console.log(columns)
console.log(rows)
  
  export default function DataTable() {
    return (
      <div style={{ height: 400, width: '100%' }}>
        <DataGrid
          rows={rows}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: { page: 0, pageSize: 5 },
            },
          }}
          pageSizeOptions={[5, 10]}
          checkboxSelection
        />
      </div>
    );
  }