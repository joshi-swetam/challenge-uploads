const url = " https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";

let samples;

let d3Output = d3.json(url).then(function(data){

    samples = data;

    const cmbNames = d3.select("#selDataset");

    samples.names.forEach((sample) => {
        cmbNames
            .append("option")
            .text("Sample " + sample)
            .property("value", sample);
    });

    //dispatch on change event to render charts
    cmbNames.dispatch("change");
    
});

// Function called by DOM changes
function optionChanged(value) {
    showTop10OTUs(value);
    showBubbleChart(value);
    showDemographicInformation(value);
    showGuague(value);
};

function getSelectedSample(value) {
    // select sample based on id
    return samples.samples.filter(
        function(sample)
        { 
            return sample.id == value ;
        })[0];
}

function getSelectedMetadata(value) {
    // select sample based on id
    return samples.metadata.filter(
        function(sample)
        { 
            return sample.id == value ;
        })[0];
}

function getSelectedSampleOTUs(value) {
    // select sample based on id
    const selectedSample = getSelectedSample(value);
    
    // create a list of dictionaries by combining list for otu ids, labels and values
    var selectSampleOTUs = [];

    selectedSample.otu_ids.forEach(function (key, i){
        var result = {};

        result['otu_id'] = key;
        result['otu_label'] = selectedSample.otu_labels[i];
        result['otu_value'] = selectedSample.sample_values[i];

        selectSampleOTUs.push(result);
    });

    return selectSampleOTUs;
}

function showTop10OTUs(value) {
    // create a list of dictionaries by combining list for otu ids, labels and values
    var selectSampleOTUs = getSelectedSampleOTUs(value);

    //sort and select top 10 otus for selected individual
    top10otus = selectSampleOTUs.sort(function(a, b){return b.otu_value - a.otu_value;}).slice(0, 10);

    //render horizontal bar chart using plotly
    let trace1 = {
        x: top10otus.map((el) => { return el.otu_value }),
        y: top10otus.map((el) => { return 'OTU ' + el.otu_id }),
        text: top10otus.map((el) => { return el.otu_label }),
        type: 'bar',
        orientation: 'h', // set orientation to horizontal
        transforms: [{  // apply a transform to render bar chart in descending order
            type: 'sort',
            target: 'y',
            order: 'descending'
            }]
    };
    
    // create a trace object
    let data = [trace1];

    // create a layout object. empty in this case as no layout requirements specified
    let layout = {
    };
    
    // render the plot
    Plotly.newPlot("bar", data, layout);
}

function showBubbleChart(value) {
    // create a list of dictionaries by combining list for otu ids, labels and values
    const selectSampleOTUs = getSelectedSampleOTUs(value);

    const otu_ids  = selectSampleOTUs.map((el) => { return el.otu_id });
    const sample_values = selectSampleOTUs.map((el) => { return el.otu_value });
    const otu_labels  = selectSampleOTUs.map((el) => { return el.otu_label });

    var trace1 = {
        x: otu_ids,
        y: sample_values,
        text: otu_labels,
        mode: 'markers',
        marker: {
            color: otu_ids,
            size: sample_values,
            colorscale: 'YlGnBu'
        }
        };
        
        var data = [trace1];
        
        var layout = {
        xaxis: {
            title: "OTU ID"
        },
        showlegend: false,
        };
        
        Plotly.newPlot('bubble', data, layout);
}

function showDemographicInformation(value) {
    selectedMetadata = getSelectedMetadata(value);
    
    const panelBody = d3.select("#sample-metadata");
    
    panelBody.html('');
    panelBody.append('div').text("  id: " + selectedMetadata.id);
    panelBody.append('div').text("  ethnicity: " + selectedMetadata.ethnicity);
    panelBody.append('div').text("  gender: " + selectedMetadata.gender);
    panelBody.append('div').text("  age: " + selectedMetadata.age);
    panelBody.append('div').text("  location: " + selectedMetadata.location);
    panelBody.append('div').text("  bbtype: " + selectedMetadata.bbtype);
    panelBody.append('div').text("  wfreq: " + selectedMetadata.wfreq);

}
function showGuague(value) {
    selectedMetadata = getSelectedMetadata(value);

    var trace = {
          type: "indicator",
          mode: "gauge+number",
          value: selectedMetadata.wfreq,
          title: { text: "Belly Button Washing Frequency Scrubs per Week", font: { size: 20 } },
          ids: ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9"],
          gauge: {
                axis: { 
                    range: [0,9],
                    tickmode: "array",
                    tickvals : [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    ticktext: ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9"],
                },
                borderwidth: 2,
                bordercolor: "gray",
                bar: {
                    color:"darkgray"
                },
                bgcolor: "lightgray"
            }
        };
      
      var layout = {
        width: 500,
        height: 400,
        margin: { t: 25, r: 25, l: 25, b: 25 },
        font: { color: "black", family: "Arial" }
      };

    var data = [trace];

    Plotly.newPlot('gauge', data, layout);
  }

