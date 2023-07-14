// Export to PDF
document.getElementById("exportPdfBtn").addEventListener("click", function() {
    // Generate your PDF content here using the pdfmake library
    const pdfContent = {
      content: [
        "Your PDF content goes here"
      ]
    };
  
    // Generate and download the PDF
    pdfmake.createPdf(pdfContent).download("exported_data.pdf");
  });
  
  // Export to Excel
  document.getElementById("exportExcelBtn").addEventListener("click", function() {
    // Generate your Excel data here using the xlsx library
    const excelData = [
      ["Header 1", "Header 2"],
      ["Value 1", "Value 2"]
    ];
  
    const worksheet = xlsx.utils.aoa_to_sheet(excelData);
    const workbook = xlsx.utils.book_new();
    xlsx.utils.book_append_sheet(workbook, worksheet, "Sheet1");
  
    // Generate and download the Excel file
    const excelFile = xlsx.write(workbook, { bookType: "xlsx", type: "buffer" });
    saveAs(new Blob([excelFile], { type: "application/octet-stream" }), "exported_data.xlsx");
  });
  