import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'TrainingCenter-new',
  templateUrl: './TrainingCenter-new.component.html',
  styleUrls: ['./TrainingCenter-new.component.scss']
})
export class TrainingCenterNewComponent {
  @ViewChild("TrainingCenterForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}